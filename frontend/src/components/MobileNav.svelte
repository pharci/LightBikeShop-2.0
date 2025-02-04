<script>
  export let currentURL = '/';
  import '../styles/mobilenav.css';
</script>
  
<div class="mobile-nav">
  <div class="mobile-nav-item">
    <a class="mobile-nav-item-link" href="/" title="Главная" class:active={currentURL === '/'}>
      <img src="/home-black.png" width="25" height="25" alt=""/>
      <span>Главная</span>
    </a>
  </div>

  <div class="mobile-nav-item">
    <a class="mobile-nav-item-link" href="/categories" title="Категории" class:active={currentURL === '/categories'}>
      <img src="/catalog-black.png" width="25" height="25" alt=""/>
      <span>Категории</span>
    </a>
  </div>

  <div class="mobile-nav-item">
    <a class="mobile-nav-item-link" href="/cart" title="Корзина" class:active={currentURL === '/cart'}>
      <img src="/cart-black.png" width="25" height="25" alt=""/>
      <span>Корзина</span>
    </a>
  </div>

  <div class="mobile-nav-item">
    <a class="mobile-nav-item-link" href="/faq" title="FAQ" class:active={currentURL === '/faq'}>
      <img src="/faq-black.png" width="25" height="25" alt=""/>
      <span>FAQ</span>
    </a>
  </div>

  <div class="mobile-nav-item">
    <a class="mobile-nav-item-link" href="/profile" title="Профиль" class:active={currentURL === '/profile'}>
      <img src="/user.png" width="25" height="25" alt=""/>
      <span>Профиль</span>
    </a>
  </div>
</div>