<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <link rel="stylesheet" href="https://cdn.bootcss.com/highlight.js/9.12.0/styles/atom-one-light.min.css" />
  <link rel="stylesheet" href="https://cdn.bootcss.com/github-markdown-css/2.8.0/github-markdown.min.css" />
  <title>Hello World，ここが私の日本空間！</title>
</head>
<body>
  <template type="markdown">
    


<!-- The (first) h1 will be used as the <title> of the HTML page -->
### <a href="#">介绍</a>
<!-- The paragraph after the h1 and ul and before the first h2 is optional. It
is intended to be used for a short summary. -->

2014年(にせんじゅうよねん)はBoston大学を研究生卒業し卒業てから，San Jose Broadcom，に行きました，働いていました，switchスイッチのtestテストを担当し(たんとう)ていました。

2016年(にせんじゅうるく)上海 Nokiaに行きました，ont，olt，システムネットワーク機器(きき)の品質保証(ひんしつほしょう)でしていました，自動化 (じどうか)升级(しんきゅう)していました，

2018年(にせんじゅうはちねん) 深圳（しんせん）Huaweiに行きました，CPU开発(かいはつ)していました，linux，dpdk，だんち＞のmaintenanceしていました。

2022年(にせんにじゅうにねん)，自分で会社（かいしゃ）立ち上げました，业务 (ぎょうむ)はWeChatのmini program，計(けい)10件(じゅうけん)ちゅうもんしで，経営(けいえいする)が行き詰（つ）まっていました，会社を譲渡(じょうと)しました。

いま，新しい挑戦(ちょうせん)をしています，闻き取りありがとうございます，大部，以上。

<!-- The unordered list immediately after the h1 will be formatted on a single
line. It is intended to be used for contact details -->
- <fanqiang320@gmail.com>
- <a href="#">+14388289640</a>
- Montréal, QC
<!-- 私は赵子肖と申します、35歳，専攻(せんこう)は电子工程(でんしこうがくか)です。 -->

### <a href="履历.xlsx">履历</a>
    ==== https://www.kobo.com/hk/en/search?query=%E9%B2%81%E9%80%9F&fclanguages=zh&pagenumber=1&sort=PublicationDateDesc&fcsearchfield=author&ac.author=%E9%B2%81%E9%80%9F
    
  </template>
    <div>
        <h3>上传</h3>
        <input type="file" id="file-uploader">

        <div id="feedback"></div>

        <label id="progress-label" for="progress"></label>
        <progress id="progress" value="0" max="100"> </progress>
    </div>
    
</body>

<script>
    const fileUploader = document.getElementById('file-uploader');
    const feedback = document.getElementById('feedback');
    const progress = document.getElementById('progress');

    const reader = new FileReader();

    fileUploader.addEventListener('change', (event) => {
        const files = event.target.files;
        const file = files[0];
        reader.readAsDataURL(file);

        reader.addEventListener('progress', (event) => {
            if (event.loaded && event.total) {
                const percent = (event.loaded / event.total) * 100;
                progress.value = percent;
                document.getElementById('progress-label').innerHTML = Math.round(percent) + '%';

                if (percent === 100) {
                    let msg = `<span style="color:green;">File <u><b>${file.name}</b></u> has been uploaded successfully.</span>`;
                    feedback.innerHTML = msg;
                }
            }
        });
    });

</script>

<script src="https://cdn.bootcss.com/marked/0.3.6/marked.min.js" charset="utf-8"></script>
<script src="https://cdn.bootcss.com/highlight.js/9.12.0/highlight.min.js" charset="utf-8"></script>
<script src="https://cdn.bootcss.com/highlight.js/9.12.0/languages/javascript.min.js" charset="utf-8"></script>
<script src="md_html.min.js" charset="utf-8"></script>
<script type="text/javascript">
  markedInHtml.init()
</script>
</html>
