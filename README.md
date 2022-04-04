# UserDict4Papago
파파고 일한 번역에 커스텀 고유명사 사전 적용하기

# 개발 환경
- Python 3.7.4 64bit
<br>
- MeCab 64bit (반드시 설치해야합니다.)
    - https://github.com/ikegami-yukino/mecab/releases
<br>
- Pip Requirements
    - mecab
    - requests
    - ko-pron
    - jaconv

# 사용법
```
git clone https://github.com/kdrkdrkdr/UserDict4Papago
cd UserDict4Papago
pip install -r requirements.txt
python main.py
```

### userdic\UserDict.txt 작성하는 법
일본어_이름,한국어_이름 으로 입력해주시면 됩니다. 정규식 지원 X
```
// Oregairu
比企谷,히키가야
八幡,하치만
小町,코마치
```