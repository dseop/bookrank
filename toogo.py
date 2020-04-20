from bs4 import BeautifulSoup as bs
from pandas import DataFrame as df
import crawling as cr

tbody_html = """<tbody>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6864');">
                                    <td>234</td>
                                    <td>길벗 이지톡</td>
                                    <td>전지연 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>아끼는 것이 자존감이다</td>
                                    <td>2020-04-20</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6861');">
                                    <td>233</td>
                                    <td>길벗 이지톡</td>
                                    <td>김복기 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>서클, 공감, 연결 - 코로나 바이러스 시대를 사는 사람들을 위한 공감 레시피</td>
                                    <td>2020-04-18</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6858');">
                                    <td>232</td>
                                    <td>길벗 이지톡</td>
                                    <td>송소정 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>脳が10歳若返る！１分脳活) (가제 : 1분 뇌 활동-뇌가 10살 젊어진다</td>
                                    <td>2020-04-17</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6846');">
                                    <td>231</td>
                                    <td>길벗 이지톡</td>
                                    <td>김남정 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>부동산 전쟁</td>
                                    <td>2020-04-10</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6844');">
                                    <td>230</td>
                                    <td>길벗 이지톡</td>
                                    <td>이민우 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>시간이 주는 기회</td>
                                    <td>2020-04-10</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6841');">
                                    <td>229</td>
                                    <td>길벗 이지톡</td>
                                    <td>추성엽 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>마케터로 비상하라</td>
                                    <td>2020-04-09</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6836');">
                                    <td>228</td>
                                    <td>길벗 이지톡</td>
                                    <td>송소정 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>기대치를 뛰어넘는다-내가 실패하며 배운 일하는 방법(期待値を超える 僕が失敗しながら学んできた仕事の方法)</td>
                                    <td>2020-04-06</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6834');">
                                    <td>227</td>
                                    <td>길벗 이지톡</td>
                                    <td>허현 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>BMW와 경영 경제 브랜딩 그리고 관광학</td>
                                    <td>2020-04-03</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6824');">
                                    <td>226</td>
                                    <td>길벗 이지톡</td>
                                    <td>이종봉 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>이제 제대로 게으르게 일해야 한다!</td>
                                    <td>2020-03-30</td>
                                    <td>대기</td>
                                </tr>
                                <tr style="cursor:pointer" onclick="javascript:move_url('6822');">
                                    <td>225</td>
                                    <td>길벗 이지톡</td>
                                    <td>이민우 [비로그인]</td>
                                    <td>경제경영 : 재테크, 비즈니스, 마케팅, 경영, 경제지식 등</td>
                                    <td>시간이 주는 기회</td>
                                    <td>2020-03-30</td>
                                    <td>대기</td>
                                </tr>
                        </tbody>"""
# url = 'https://gbadmin.gilbut.co.kr/customer/author_recruit?search_date=&gr_strdate=&gr_enddate=&search_cate1=004000&search_cate2=004001&search_state=&search_F=GR_NAME&search_S='
# tmp_par = cr.makepar(url)

par_url = bs(tbody_html, 'html.parser')

tr_list = par_url.find_all('tr')
td_list = []
for i in tr_list :
    td_list.append(i.get_text('/', strip=True).split('/'))

result_1 = []
result_2 = []
result_3 = []
for k in td_list :
    result_1.append(k[5])
    result_2.append(k[4])
    result_3.append(k[2][:3])

df({
    'date': result_1,
    'title': result_2,
    'name': result_3,
}).to_csv('getinfo.csv', header=True, index=True, encoding='ms949')