export class GP {
    constructor(id) {
        this.id = id;
        this.$gp = $('#' + id);
        this.testpage = new GPTestPage(this);
    }
}

