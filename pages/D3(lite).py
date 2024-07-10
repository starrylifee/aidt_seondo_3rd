import streamlit as st
import random
import toml
import pathlib
from openai import OpenAI
import pandas as pd

# secrets.toml 파일 경로
secrets_path = pathlib.Path(__file__).parent.parent / ".streamlit/secrets.toml"

# secrets.toml 파일 읽기
with open(secrets_path, "r") as f:
    secrets = toml.load(f)

# 여러 API 키 값 가져오기
api_keys = [secrets.get(f"api_key{i}") for i in range(1, 4)]

# 랜덤하게 API 키를 선택하여 OpenAI 클라이언트 초기화
selected_api_key = random.choice(api_keys)
client = OpenAI(api_key=selected_api_key)

# 페르소나 특성 정의
persona_traits = ["학습집중력", "기기친숙도", "전시학습이해도", "과제집착력", "학업스트레스", "자기조절", "가정환경", "학업성취도"]
learning_preferences = ["개인학습선호", "협동학습선호"]
genders = ["boy", "girl"]

# 각 특성의 게이지를 한글로 매핑
gauge_map = {
    1: "매우 낮음",
    2: "낮음",
    3: "보통",
    4: "높음",
    5: "매우 높음"
}

# Streamlit 앱 인터페이스 구성
st.title("개발한 수업의 적절성 평가하기 🎨")
st.write("동료 선생님이 설계한 AIDT 사용 수업을 학생 입장에서 체험해 봅시다.")
st.markdown("체험한 수업이 올바르고 적절한 것인지 아래 활동을 하며 평가해 봅시다. 개선해야 한다면 이때 사용하면 좋은 AIDT기능을 떠올려 보세요.")
st.markdown("학생의 페르소나가 무작위로 생성됩니다. AI 디지털 교과서 활용 수업 설계의 원칙 카드를 이용해 학생에게 도움이 되는 수업을 설계하였는지 판단해 보세요.")

# 게임방법 강조
st.markdown("""
<div style='border: 2px solid #f39c12; padding: 10px; border-radius: 5px;'>
    <h3>게임방법 🎮</h3>
    <ul>
        <li>👥 인원수: 2~6</li>
        <li>📦 준비물: AI 디지털 교과서 활용 수업 설계의 원칙 카드 20장, AIDT카드 17장, 종</li>
        <li>🃏 AI 디지털 교과서 활용 수업 설계의 원칙 카드 20장을 똑같이 나눠 가지고 남은 것은 중앙에 쌓아 둡니다.</li>
        <li>🃏 AIDT카드는 모두 중앙에 그림이 보이게 펼쳐 둡니다.</li>    
        <li>🔍 모둠 가운데에 디지털기기를 1대를 놓고, '어떤 학생이 나타날까요?' 버튼을 누른 후 결과를 함께 봅시다. </li>
        <li>🕒 오른쪽 위의 RUNNING이 끝나면 그림과 함께 학생의 정보가 나타납니다.</li>
        <li>👀 학생의 정보와 내가 들고 있는 AI 디지털 교과서 활용 수업 설계의 원칙 카드를 살펴보고 수업을 평가해 봅시다.</li>
        <li>🔔 모둠 가운데 있는 종을 치고 해당되는 AI 디지털 교과서 활용 수업 설계의 원칙 카드를 내려놓으며 수업의 적절성 여부를 평가합니다. 개선할 때 사용하면 좋은 AIDT기능이 떠오른다면 해당 AIDT카드를 집어 주세요.(없으면 선택하지 않으셔도 됩니다.)</li>
        <li>👍 과반수가 수업에 대한 평가 내용에 동의할 경우 자신의 카드를 중앙의 카드덱에 버립니다. AIDT카드는 다시 원래 자리에 놓아 주세요.</li>
        <li>🏆 위 과정을 반복하여 제한시간 안에 가장 빨리 카드를 버린 사람이 승리합니다.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("이 이미지생성도구의 사용 비용은 서울특별시교육청 AI 에듀테크 선도교사 운영비로 지출됩니다.")
st.markdown("제작자: 서울특별시교육청융합과학교육원 정용석, 소일초등학교 김유진")

# 입력 값 검증 및 이미지 생성
if st.button("어떤 학생이 나타날까요?"):
    # 무작위로 3개의 페르소나 특성 선택
    selected_traits = random.sample(persona_traits, 3)
    selected_gauges = {trait: random.choice([1, 2, 3, 4, 5]) for trait in selected_traits}
    selected_learning_preference = random.choice(learning_preferences)
    gender = random.choice(genders)

    # 선택된 페르소나 특성 및 게이지 시각화
    selected_gauges["학습선호도"] = selected_learning_preference
    traits_df = pd.DataFrame(list(selected_gauges.items()), columns=['Trait', 'Gauge'])
    st.bar_chart(traits_df.set_index('Trait'))

# 세션 초기화 버튼
if st.button("다시 시작하기"):
    st.experimental_rerun()

st.markdown("[D3 체크리스트카드 다운로드 - 인쇄하여 사용하세요.](https://drive.google.com/drive/folders/1G10VNydf2vMAKTOaBcFfGL4sG8OAKnp_?usp=drive_link)")

# 유튜브 영상 추가
st.markdown("### 활동안내영상")
st.video("https://www.youtube.com/watch?v=UgBUfd_x3UQ")
