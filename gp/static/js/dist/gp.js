class GPTestPage {
    constructor(root) { // 传进来的root就是GP的对象
        this.root = root;
        this.$testpage = $(`
<div class="gp-testpage">
    <div class="gp-testpage-field">
		<div class="gp-testpage-title">
           网络暴力语言测试
		</div>
        <div class="gp-testpage-input">
            <div class="gp-testpage-item">
                <input type="text" placeholder="请输入测试语句">
            </div>
        </div>
        <div class="gp-testpage-val">
            <div class="gp-testpage-item">
                <button> 验证 </button>
            </div>
        </div>
        <div class="gp-testpage-return">
            <div class="gp-testpage-item">
                <img src="static/images/test_page/yes.png">
            </div>
        </div>
    </div>
</div>

`)// 如果是html对象前面加上$
        this.$testpage_input = this.$testpage.find(".gp-testpage-input input");
        this.$testpage_val = this.$testpage.find(".gp-testpage-val button");
        this.$testpage_image = this.$testpage.find(".gp-testpage-return img");

        this.root.$gp.append(this.$testpage);

        this.start();
    }

    start() {
        this.add_listening_event();
    }

    add_listening_event() {
        let outer = this;

        this.$testpage_val.click(function() {
            outer.validation_input();
        });
    }

    validation_input() {
        let outer = this;
        let text = this.$testpage_input.val();
        
        $.ajax({
            url: "http://124.222.103.9:9000/test_page/getinfo/",
            type: "GET",
            data: {
                text: text,
            },
            success: function(resp) {
                if (resp.result === "success") {
                    outer.$testpage_image.attr('src', resp.val_return);
                }
            }
        });
    }

}
export class GP {
    constructor(id) {
        this.id = id;
        this.$gp = $('#' + id);
        this.testpage = new GPTestPage(this);
    }
}

