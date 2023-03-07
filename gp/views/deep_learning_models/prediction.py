import jieba
import pickle

from jieba import analyse
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPool1D, Bidirectional, LSTM, Dropout, Flatten, Dense

# 中文分词
def chinese_word_cut(row):
    return " ".join(jieba.cut(row))


# 提取关键词
def key_word_extract(texts):
    # topK:表示提取前50个关键词，withWeight:是否考虑权重，allowPOS=()表示不限制词性
    return " ".join(analyse.extract_tags(texts, topK=50, withWeight=False, allowPOS=()))

def create_model():
    model = Sequential()
    model.add(Embedding(output_dim=64, input_dim=2000, input_length=50))

    # 卷积层
    model.add(Conv1D(filters=128, kernel_size=2, padding='same', activation='relu'))
    # 卷积核 128 卷积核大小 2 保持输出大小与输入大小一致 激活函数为relu
    model.add(MaxPool1D(3, 2))
    # 最大池化层大小 3 步长 2
    model.add(Conv1D(filters=64, kernel_size=3, padding='same', activation='relu'))
    model.add(MaxPool1D(3, 2))
    model.add(Conv1D(filters=32, kernel_size=5, padding='same', activation='relu'))
    model.add(MaxPool1D(3, 2))

    # BiLSTM层
    model.add(Bidirectional(LSTM(64, return_sequences=True)))
    # 64个LSTM单元
    model.add(Dropout(0.4))

    # 展平层
    model.add(Flatten())

    # 输出层
    model.add(Dense(units=1, activation='sigmoid'))

    # 编译模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model

def text_prediction(text):
    # 加载模型
    model = create_model()
    model.load_weights('/home/yyj/yyjapp/gp/views/deep_learning_models/bully_CNN_BiLSTM_text.h5')

    with open('/home/yyj/yyjapp/gp/views/deep_learning_models/tokenizer.pickle', 'rb') as handle:
        token = pickle.load(handle)

    text_cut = chinese_word_cut(text)
    text_key = key_word_extract(text_cut)
    text_seq = token.texts_to_sequences([text_key])
    text_seq_padding = sequence.pad_sequences(text_seq, maxlen=50)

    prediction = model.predict(text_seq_padding)

    print(prediction)

    if prediction > 0.5:
        return 1
    else:
        return 0

