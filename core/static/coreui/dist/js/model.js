function submitInfo() {
        // 获取模型信息
        var activeButton = document.querySelector("button.nav-link.active");
        var info = activeButton.innerText;

        // 获取当前URL
        var currentUrl = window.location.href.split('?')[0].split('#')[0];

        // 发起 AJAX 请求提交信息
        var xhr = new XMLHttpRequest();
        xhr.open("POST", currentUrl, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        // 处理请求完成后的回调
        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                // 请求成功处理逻辑
                console.log("信息提交成功");
            } else {
                // 请求失败处理逻辑
                console.error("信息提交失败");
            }
        };

        // 发送包含信息的 JSON 数据
        xhr.send(JSON.stringify({'current_model': info, 'action': 'info'}));
    }
function refresh() {
        const delayInMilliseconds = 1000; // 2秒
        setTimeout(function() {
            // 刷新当前页面
            location.reload();
        }, delayInMilliseconds);
    }
