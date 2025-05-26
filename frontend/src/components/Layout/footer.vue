<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="company-info">
        <h3>모예모에 컴퍼니</h3>
        <p>대표이사: 김예나, 이진모</p>
        <p>연락처: 010-7568-8524</p>
      </div>
      <div class="footer-links">
        <div class="link-group">
          <h4>About Us</h4>
          <ul>
            <li>회사 소개</li>
            <li>이용약관</li>
            <li>개인정보처리방침</li>
          </ul>
        </div>
        <div class="link-group">
          <h4>Contact</h4>
          <ul>
            <li>고객센터</li>
            <li>제휴문의</li>
            <li>광고문의</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2024 모예모에 컴퍼니. All rights reserved.</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: rgb(46, 46, 46);
  color: #fff;
  padding: 3rem 0 1.5rem;
  margin-top: 4rem;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  gap: 2rem;
}

.company-info {
  flex: 1;
}

.company-info h3 {
  color: #4CAF50;
  font-size: 1.5rem;
  margin: 0 0 1rem;
}

.company-info p {
  color: #999;
  margin: 0.5rem 0;
  font-size: 0.9rem;
}

.footer-links {
  display: flex;
  gap: 4rem;
}

.link-group h4 {
  color: #4CAF50;
  margin: 0 0 1rem;
  font-size: 1rem;
}

.link-group ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.link-group li {
  color: #999;
  margin: 0.5rem 0;
  font-size: 0.9rem;
  cursor: pointer;
  transition: color 0.2s ease;
}

.link-group li:hover {
  color: #4CAF50;
}

.footer-bottom {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-bottom p {
  color: #666;
  font-size: 0.8rem;
  margin: 0;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
  }

  .footer-links {
    justify-content: center;
    gap: 2rem;
  }

  .link-group {
    text-align: left;
  }
}
</style>
