# RVC WebAPI

- gradio_clientを使ったRVCのWebAPI実装のサンプルです
- rvctts は https://github.com/litagin02/rvc-tts-webui が必要
  - 作者さんも私も Style-Bert-VITS2 に移行してしまったため使う機会が無くなってしまった
- それ以外は、本家RVC(だったと思う)か、ひょっとしたら Applio 用
  - 仮のコードなので API の仕様をきちんと調べてない
  - https://huggingface.co/spaces/aka7774/gradio_client_api_viewer で調べられます

## 今後RVCをWebAPIで使いたい時の戦略案

- Applio を使う?
  - なんかWebAPIの情報がクラウドサービスしか見つからなくない?
- https://github.com/ddPn08/rvc-webui を使う
  - 作者さんが「飽きたのでもうやらない」と宣言しているので将来性は無い
  - 古いRVC資産を活かしたいしかならアリかも
- このサンプルのようにgradio_clientを使う
  - RVC本家も飽きてそうなのでポジティブに考えれば更新に追従する手間はほぼ無さそう
  - 現時点で最新のwebsocketsに対応してなくて他と同居できないのでvenvを切り分けるのが良さそう
