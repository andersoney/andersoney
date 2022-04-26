class A {
    call(func1, func2, where) {
        func1(where).then(func2).catch(this.callbackError)
    }
    callbackError(error) {

    }
}
class B extends A {
    async findByCode() {

    }
    executeProcess() {
        let dataConvert = (data) => {

        }
        this.call(this.findByCode, dataConvert, { where: { code: "123" } })
    }
}