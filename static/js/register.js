$(function () {

    function bindCaptchaBtnClick() {

        $("#captcha-btn").click(function (event) {
            let $this = $(this);
            let email = $("input[name='email']").val()
            if (!email) {
                alert("请输入邮箱")//弹出提示框
                return;
            }
            //取消按钮的点击事件
            $this.off("click");

            //发送ajax请求
            $.ajax('/auth/captcha?email=' + email, {
                method: "GET",
                success: function (result) {
                    if (result['code'] == 200) {
                        alert("验证码发送成功")
                    } else {
                        alert("验证码发送失败")
                    }
                    console.log(result);
                },
                fail: function (error) {
                    console.log(error);
                }
            })

            let countdown = 6;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text("获取验证码");
                    clearInterval(timer);//清除定时器
                    //重新绑定点击事件
                    bindCaptchaBtnClick()
                } else {
                    $this.text(countdown + "秒后重新获取");
                    countdown--;
                }

            }, 1000)
        })
    }

    bindCaptchaBtnClick();
});