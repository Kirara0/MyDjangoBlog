$(document).ready(function () {


    // 发布按钮点击事件
    $("#submit-btn").click(function (event) {
        event.preventDefault();//阻止表单默认提交

        let title = $("input[name='title']").val()
        let category = $("#id_category").val()
        let content = $("textarea[name='content']").val()
        let csrfToken = $("input[name='csrfmiddlewaretoken']").val()

        if (!title) {
            alert("请输入标题")//弹出提示框
            return;
        }
        if (!category) {
            alert("请选择标签")//弹出提示框
            return;
        }
        if (!content) {
            alert("请输入内容")//弹出提示框
            return;
        }
        // 发送ajax请求
        $.ajax('/blog/public/', {
            method: "POST",
            data: {
                title: title,
                category: category,
                content: content,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function (result) {
                if (result['code'] == 200) {
                    console.log("准备跳转，ID:", result.id);
                    alert("即将跳转到详情页，ID: " + result.id); // 👈 临时加这行
                    // 使用 setTimeout 延迟跳转（避开某些扩展的即时拦截）
                    setTimeout(() => {
                        window.location.href = `/blog/detail/${result.id}/`;
                    }, 100);
                } else {
                    alert("发布失败")
                }
                console.log(result);
            },
        });

    })
});