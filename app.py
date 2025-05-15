import os
from flask import Flask, render_template, url_for
import json # json 라이브러리 추가

app = Flask(__name__)

# --- 중요 설정 ---
# Teachable Machine 모델에서 사용한 클래스 이름과 static/characters 폴더 안의 이미지 파일 이름을 매칭시킵니다.
# 모델의 metadata.json 파일에 있는 labels 배열 순서와 이름을 정확히 확인하고 작성하세요!
CHARACTER_IMAGE_MAP = {
    "탄지로": "카마도_탄지로_0.jpg",  # 예시: 모델 클래스 이름 -> 이미지 파일 이름
    "네즈코": "네즈코_0.jpg",
    "이노스케": "하시바라_이노스케_0.jpg",
    "텐겐":"우즈이_텐겐_0.jpg",
    "쿄쥬로":"렌고쿠_쿄쥬로_0.jpg",
    "시노부":"코쵸우_시노부_0.jpg",
    "기유":"토미오카_기유_0.jpg",
    "교메이":"히메지마_교메이_0.jpg"
    # 여기에 모델의 모든 클래스 이름과 해당하는 이미지 파일 이름을 추가하세요.
    # "클래스이름4": "이미지파일4.jpg",
}
CHARACTER_IMAGE_MAP1 = {
    "소류 아스카 랑그레이": "소류_아스카_랑그레이_0.jpg",
    "아야나미 레이": "아야나미_레이_0.jpg",
    "이카리 겐도": "이카리_겐도_0.jpg",
    "아카기 리츠코": "akagi_ritsuko_0.jpg",
    "이카리 유이": "Ikari_yui_0.jpg",
    "카지 료지": "kaji_ryoji_0.jpg",
    "카츠라기 미사토": "katsuragi_misato_0.jpg",
    "마키나미 마리 일러스트리어스": "Mari_Illustrious_Makinami_0.jpg",
    "나기사 카오루": "nagisa_kaworu_0.jpg",
    "이카리 신지": "shinji_Ikari_0.jpg"

}

CHARACTER_IMAGE_MAP2 = {
    "한수지": "짱구는_못말려_수지_0.jpg",
    "맹구": "맹구_0.jpg",
    "원장선생님": "짱구_원장선생님_0.jpg",
    "짱아": "nohara_himawari_0.jpg",
    "훈이": "훈이_0.jpg",
    "차은주 선생님": "짱구는_못말려_차은주_0.jpg",
    "채성아 선생님": "짱구는_못말려_채성아_0.jpg",
    "봉미선": "봉미선_0.jpg",
    "한유리": "유리_짱구는_못말려_0.jpg",
    "신짱구": "신짱구_0.jpg",
    "흰둥이": "흰둥이_짱구는_못말려_0.jpg",
    "김철수": "짱구는_못말려_철수_0.jpg",
    "나미리 선생님": "나미리_0.jpg"

}
CHARACTER_IMAGE_MAP3 = {
    "시라토리 아이라": "Aira_Shiratori_DanDaDan_0.jpg",
    "엔조지 진": "Jin_Enjoji_0.jpg",
    "타카쿠라 켄": "Ken_takakura_DanDaDan_0.jpg",
    "사카타 킨타": "Kinta_Sakata_0.jpg",
    "아야세 모모": "Momo_Ayase_0.jpg",
    "아야세 세이코": "Seiko_Ayase_0.jpg",
}



# ----------------
@app.route('/')
def index():
    # 갤러리에 표시할 아이템 목록 (필요에 따라 DB 등에서 가져올 수 있음)
    gallery_items = [
        {
            "title": "귀멸의 칼날",
            "image": "posters/demon_slayer_poster.jpg", # static/posters 안의 파일명
            "link": url_for('demon_slayer_analysis') # 귀멸의 칼날 분석 페이지 라우트 함수명
        },
        {
            "title": "에반게리온", # 예시: 다른 애니메이션
            "image": "posters/evangelion.png", # 예시: 준비중 이미지
            "link": url_for('eva_analysis') # 아직 링크 없음
        },
         {
            "title": "짱구는 못말려",
            "image": "posters/shinchan.png",
            "link": url_for('shinchan')
        },
        {
            "title": "단다단",
            "image": "posters/DanDaDan.png",
            "link": url_for("DanDaDan")
        },
        {
            "title": "준비중",
            "image": "posters/placeholder.png",
            "link": "#"
        },
        {
            "title": "준비중",
            "image": "posters/placeholder.png",
            "link": "#"
        }
        # 다른 애니메이션 아이템 추가 가능
    ]
    return render_template('gallery.html', gallery_items=gallery_items)


@app.route('/demon-slayer')
def demon_slayer_analysis():
    #character_map_json = json.dumps(CHARACTER_IMAGE_MAP) # JSON 문자열로 변환
    return render_template('index.html', character_map=CHARACTER_IMAGE_MAP) 



@app.route('/eva_analysis')
def eva_analysis():
    #character_map_json = json.dumps(CHARACTER_IMAGE_MAP) # JSON 문자열로 변환
    return render_template('eva.html', character_map1 =CHARACTER_IMAGE_MAP1)

@app.route('/shinchan')
def shinchan():
    #character_map_json = json.dumps(CHARACTER_IMAGE_MAP) # JSON 문자열로 변환
    return render_template('shinchan.html', character_map1 =CHARACTER_IMAGE_MAP2)

@app.route('/DanDaDan')
def DanDaDan():
    #character_map_json = json.dumps(CHARACTER_IMAGE_MAP) # JSON 문자열로 변환
    return render_template('DanDaDan.html', character_map1 =CHARACTER_IMAGE_MAP3)  


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port= "5001", debug=True)