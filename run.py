# 네이버에서 '유미의세포들 구웅' 입력 후 검색 -> 결과
# 로그인시 PC 웹사이트에서 처리가 어려울 경우 -> 모바일 로그인으로 진입 ex. 네이버

# 모듈 가져오기
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
# 명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

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
# driver.find_element_by_css_selector('.blog>.section>._blogBase>._prs_blg').click()

# why? 서버가 늦게 뜨는 경우 대비 

# 게시판에서 데이터를 가져올때 
# 데이터가 많으면 세션(혹은 로그인을 해서 접근되는 사이트일 경우) 관리
# 특정 단위별로 로그아웃 로그인 계속 시도
# 특정 게시물이 사라질 경우 => 팝업 발생(없는 ~~~) => 팝업 처리 검토

# 게시판을 스캔시 -> 임계점을 모름!!!
# 게시판을 스캔해 => 메타 정보를 획득 => 루프를 돌려서 일괄적으로 방문 접근 처리

# 1년 크롤링
# submit_date_option('1year'); return false;

# return goOtherCR(this,'a=blg.paging&i=&r=2&u='+urlencode(urlexpand(this.href))); 스크립트 실행
# 45은 임시값, 게시물을 넘어갔을때 현상을 확인차
for page in range(1, 45):
    try:
        # 자바스크립트 구동하기
        return_value = driver.execute_script("return goOtherCR(this,'a=blg.paging&i=&r={}&u='+urlencode(urlexpand(this.href)));".format(page))
        print(return_value)
        time.sleep(2)
        print("%s 페이지 이동" % page)

    except Exception as e1:
        print('오류', e1)
