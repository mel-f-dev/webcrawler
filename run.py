# 네이버에서 '유미의세포들 구웅' 입력 후 검색 -> 결과
# 로그인시 PC 웹사이트에서 처리가 어려울 경우 -> 모바일 로그인으로 진입 ex. 네이버

# 모듈 가져오기
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
# 명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 사전에 필요한 정보 로드 -> 디비 혹은 쉘, 배치 파일에서 인자로 받아서 세팅
main_url = 'https://www.naver.com/'
keyword = '유미의세포들 구웅'

# 드라이버 로드
driver = wd.Chrome(executable_path='downloads/chromedriver.exe')  # 브라우저가 뜬다
# 차후 옵션(프록시, 에이전트 조작, 이미지를 배제) 부여하여 크롤링을 오래돌리면 임시파일들이 쌓인다!! -> 템포 파일 삭제

# 사이트 접속 (get)
driver.get(main_url)
# 검색창 찾아서 검색어 입력
# id="query"
driver.find_element_by_id('query').send_keys(keyword)
# 수정할 경우 => 뒤에 내용이 붙어버림 -> .clear() -> send_keys('내용')

# 검색 버튼 찾고 클릭
# id="search_btn"
driver.find_element_by_css_selector('#search_btn').click()

# 웨이트 -> 페이지가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는 자제
# 명시적 대기 -> 특정 요소가 로케이트(발견될 때 까지) 대기
# try:
#     element = WebDriverWait(driver, 10).until(
#         # 지정한 한 개 요소가 올라오면 웨이트 종료
#         # class="go_more"
#         EC.presence_of_element_located((By.CLASS_NAME, '.blog>.section>._blogBase>._prs_blg'))
#     )
# except Exception as e:
#     print('오류 발생', e)

# 암묵적 대기 -> DOM이 다 로드 될때까지 대기 후 로드되면 바로 진행
# 요소를 찾을 특정 시간 동안 DOM 풀링 지시 ex) 10초 이내라도 발견되면 바로 진행
driver.implicitly_wait(10)
# 절대기 대기 -> time.sleep(10) -> 클라우드 페어(디도스 방어 솔루션)

# 더보기 눌러서 새로운 페이지 진입
driver.find_element_by_link_text('블로그 더보기').click()

# why? 서버가 늦게 뜨는 경우 대비 
