<script>
    import { user } from '../stores/auth.js';
    import { Router, Route, Link } from 'svelte-routing';
    import Profile from '../pages/Profile.svelte';
    import Home from '../pages/Home.svelte';
    import Faq from '../pages/Faq.svelte';
    import Wishlist from '../pages/Wishlist.svelte';
    import Cart from '../pages/Cart.svelte';
    import Login from '../pages/Login.svelte';
    import '../styles/header.css';
</script>

<header>
    <div class="header-wrapper">
        <nav>
            <ul class="nav">
                <!-- Логотип -->
                <li class="grid-item nav-item logo">
                    <Link class="nav-link" to="/">
                        LightShop
                    </Link>
                </li>

                <!-- Поиск -->
                <li class="grid-item search">
                    <div class="input-field">
                        <input class="search-field" name="q" type="text" placeholder="Поиск" />
                        <div class="input-field--buttons">
                            <button type="submit" class="search-submit" aria-label="Поиск">
                                <img src="/search-icon.png" width="20" height="20" alt="Поиск" />
                            </button>
                            <div class="separator"></div>
                            <button type="reset" class="search-cancel" aria-label="Отмена">
                                <img src="/cancel.png" width="20" height="20" alt="Отмена" />
                            </button>
                        </div>
                    </div>
                </li>

                <!-- Действия в шапке -->
                <div class="grid-item header-actions">
                    <li class="nav-item">
                        <Link class="nav-link" to="/faq">
                            <img src="/faq-black.png" width="25" height="25" alt="FAQ" />
                            <span>FAQ</span>
                        </Link>
                    </li>
                    <li class="nav-item">
                        <Link class="nav-link" to="/wishlist">
                            <img src="/heart.png" width="25" height="25" alt="Избранное" />
                            <span>Избранное</span>
                        </Link>
                    </li>
                    <li class="nav-item">
                        <Link class="nav-link" to="/cart">
                            <img src="/cart-black.png" width="25" height="25" alt="Корзина" />
                            <span>Корзина</span>
                        </Link>
                    </li>

                    {#if $user}
                        <li class="nav-item">
                            <Link class="nav-link" to="/profile">
                                <img src="/user.png" width="25" height="25" alt="Профиль" />
                                <span>Профиль</span>
                            </Link>
                        </li>
                    {:else}
                        <li class="nav-item">
                            <Link class="nav-link" to="/login">
                                <img src="/login.png" width="25" height="25" alt="Войти" />
                                <span>Войти</span>
                            </Link>
                        </li>
                    {/if}
                </div>

                <!-- Категории -->
                <div class="header-categories">
                    <li class="nav-item">
                        <Link class="nav-link" to="/">Запчасти</Link>
                    </li>
                    <li class="nav-item">
                        <Link class="nav-link" to="/">Одежда</Link>
                    </li>
                    <li class="nav-item">
                        <Link class="nav-link" to="/">Мастерская</Link>
                    </li>
                </div>
            </ul>
        </nav>
    </div>
</header>

<Router>
    <Route path="/" component={Home} />
    <Route path="/faq" component={Faq} />
    <Route path="/wishlist" component={Wishlist} />
    <Route path="/cart" component={Cart} />
    <Route path="/profile" component={Profile} />
    <Route path="/login" component={Login} />
</Router>