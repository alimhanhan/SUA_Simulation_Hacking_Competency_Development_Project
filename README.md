# ⚔️SUA 역량발전 모의해킹 & 취약점 탐색 프로젝트⚔️

<br><h2>🏆Step_1) 취약점 탐지 환경 구축</h2>
<h3>♟️Used Tech Stack</h3>
: Django ( 장고 ) & Pythonanywhere<br>

<br><h3>♟️Implemented Services</h3>
1. 회원가입 및 로그인 기능
2. 게시판 글 목록 조회 기능
3. 게시판 글 작성 및 삭제, 수정 기능
4. 게시판 댓글 작성 및 삭제, 수 기능
5. 게시판 글 구성 기능 ( 제목, 작성자, 작성일, 본문으로 구성 )
6. 게시판 글 검색 기능
7. 게시판 글, 댓글 추천 기능
8. 서비스 관리자 로그인 서비스
9. 서비스 관리자 페이지 구현
10. ( 서비스 관리자 한정 ) 타인이 작성한 글 삭제 서비스<br><br>

<h3>♟️Access ink</h3>
--> https://kadraw.pythonanywhere.com/pybo/](https://kadraw.pythonanywhere.com/pybo/

![Untitled](https://user-images.githubusercontent.com/102565567/232185322-5642635f-e0b4-4af1-aaaa-ef44f935012e.png)

<br><br><h2>🏆Step_2) Web 공방전 및 실시간 보안 패치</h2>
<h3>♟️Duration of Vulnerability Scanning</h3>
: 2023/01/28 15:00 ~ 2023/02/05 23:59<br><br>

<details>
<summary> 📢Rules related to Vulnerability Reporting</summary>
<div markdown="1">

<br>**🚨 취약점 발견 시**

- 단체 메신저에 아래의 양식을 통해 취약점 제보
- ✅ 표시 시, 취약점 접수 완료 (점수 반영)

```
🚨 취약점 제보

target : <http://124.60.4.10:6662/write_action.php>
payload : burp로 post parameter 변조, text=attack;!@
impact : 해커의 악의적인 포스팅 작성으로 인한 게시판 사용자에 대한 피싱 공격 가능
  
+공격 성공 스크린샷 첨부
```

※ impact는 파급력으로, 상세히 작성<br>
※ 공격자는 취약점 제보 시 조치 방안 관련 내용을 제외하여 제보<br>
※ 공방전에서 장애 유발 행위 일체 금지<br>

</div>
</details>
<details>
<summary>📢Rules related to Security Measures</summary>
<div markdown="1">

 <br> **🛡 보안 조치 완료 시**

- 단체 메신저에 아래의 양식을 통해 보안 조치 완료 보고
- ✅ 표시 시, 보안 조치 확인 완료(점수 반영)

```
🛡 보안 조치 완료

target : <http://124.60.4.10:6662/write_action.php>
payload : burp로 post parameter 변조, text=attack;!@
  
+취약점 제보자가 제공한 payload 공격을 그대로 재연하였을 때의 방어 성공 스크린샷 첨부
```

※ 보안 조치 중 장애 유발 행위에 유의
</div>
</details>
<details>
<summary>📢Rules related to Scores</summary>
<div markdown="1"><br>

**🚩 참고사항 🚩**

- 모의해킹 보고서 상 있던 취약점들도 조치가 안되었다면, 모두 제보 가능
- 첫번째 공격 제보자만 점수 부여
- 보안 조치에 보다 높은 점수 부여

</div>
</details>

<br><h2>🏆Step_3) 발견 사항 검토 및 사후 보고서 작성</h2>
: Web 공방전을 통해 발견한 취약점들을 기반으로 사후 보고서 작성
