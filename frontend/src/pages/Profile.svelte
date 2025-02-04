<script>
    import { user } from '../stores/auth.js';
    console.log($user)
</script>

<h1>Профиль</h1>
{#if $user}
    <p>Привет, {$user.username}!</p>
{:else}
    <p>Пожалуйста, войдите в систему.</p>
{/if}