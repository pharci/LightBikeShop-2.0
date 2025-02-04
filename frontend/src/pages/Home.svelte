<script>
    import { user } from '../stores/auth.js';
    console.log(document.cookie);
</script>

<h1>Главная страница</h1>
<p>Добро пожаловать на LightShop!</p>
{#if $user}
    <p>Привет, {$user.username}!</p>
{:else}
    <p>Пожалуйста, войдите в систему.</p>
{/if}