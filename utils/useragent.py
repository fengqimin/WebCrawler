# http://useragentstring.com/pages/useragentstring.php
# 桌面端
__all__ = ["USER_AGENT_DESKTOP", "USER_AGENT_MOBILE", "random_ua"]

USER_AGENT_DESKTOP = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.4) Gecko/20100101 Firefox/60.4',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.5) Gecko/20100101 Firefox/60.5",
]

# 移动端
USER_AGENT_MOBILE = [
    'Mozilla/5.0 (iPhone; CPU OS 10_14 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Mobile/14E304 Safari/605.1.15',
    'Mozilla/5.0 (iPad; CPU OS 10_14 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Mobile/15E148 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 9.0; Z832 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
    'Mozilla/5.0 (Android 9.0; Mobile; rv:64.0) Gecko/64.0 Firefox/64.0',
    'Mozilla/5.0 (Linux; Android 9.0; SAMSUNG-SM-T377A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
]

# 其它
USER_AGENT_OTHER = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'curl/7.63.0',
    'Wget/1.20.1 (linux-gnu)',
    'Mozilla/5.0 (PlayStation 4 4.71) AppleWebKit/601.2 (KHTML, like Gecko)'
]

# ---------------------------------------------------------
# 参考了火狐插件user-agent-switcher中的UA字符串
# https://gitlab.com/ntninja/user-agent-switcher
# ---------------------------------------------------------
DESKTOP = {
    "Windows / Firefox 64 [Desktop]":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    "Linux / Firefox 64 [Desktop]":
        "Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0",
    "Mac OS X / Safari 11.1.1 [Desktop]":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15",
    "Windows / IE 11 [Desktop]":
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Windows / Edge 17 [Desktop]":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Windows / Chrome 71 [Desktop]":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Windows / Firefox 60 ESR [Desktop]":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.4) Gecko/20100101 Firefox/60.4"
}

MOBILE = {
    "Android Phone / Firefox 64 [Mobile]":
        "Mozilla/5.0 (Android 9.0; Mobile; rv:64.0) Gecko/64.0 Firefox/64.0",
    "Android Phone / Chrome 71 [Mobile]":
        "Mozilla/5.0 (Linux; Android 9.0; Z832 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "Android Tablet / Chrome 71 [Mobile]":
        "Mozilla/5.0 (Linux; Android 9.0; SAMSUNG-SM-T377A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "iPhone / Safari 11.1.1 [Mobile]":
        "Mozilla/5.0 (iPhone; CPU OS 10_14 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Mobile/14E304 Safari/605.1.15",
    "iPad / Safari 11.1.1 [Mobile]":
        "Mozilla/5.0 (iPad; CPU OS 10_14 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Mobile/15E148 Safari/605.1.15",
}

OTHER = {
    "Google Bot [Bot]": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "PS4 [Other]": "Mozilla/5.0 (PlayStation 4 4.71) AppleWebKit/601.2 (KHTML, like Gecko)",
    "Curl [Other]": "curl/7.63.0",
    "Wget [Other]": "Wget/1.20.1 (linux-gnu)"
}


def random_ua(terminal_type: str = 'Desktop') -> str:
    from random import choice
    """随机返回user-agent字符串"""
    if not isinstance(terminal_type, str):
        print('请选择终端类型：Desktop Mobile or Other, default is Desktop')
    if terminal_type.lower() == 'desktop':
        return choice(USER_AGENT_DESKTOP)
    elif terminal_type.lower() == 'mobile':
        return choice(USER_AGENT_MOBILE)
    elif terminal_type.lower() == 'other':
        return choice(USER_AGENT_OTHER)
    else:
        print('请选择终端类型：desktop mobile or other')
        return ''


if __name__ == '__main__':
    ua_string = random_ua()
    print(ua_string)
