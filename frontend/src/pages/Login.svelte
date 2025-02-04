<script>
    import { setUser } from '../stores/auth.js';

    let username = "";
    let password = "";
    let message = ""; // Сообщение для вывода ошибок

    async function login() {
        if (!username || !password) {
            message = "Введите логин и пароль.";
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include',
                body: JSON.stringify({ username, password })
            });
            if (response.ok) {
                const userData = await response.json();
                setUser(userData);
                console.log(userData)
            } else {
                const error = await response.json();
                message = `Ошибка: ${error.detail || 'Неизвестная ошибка'}`;
            }
        } catch (error) {
            message = `Ошибка: ${error.message}`;
        }
    }

    // Перемещение фокуса или авторизация по клавише Enter
    function handleKeydown(event) {
        if (event.key === "Enter") {
            if (document.activeElement === document.querySelector("#username")) {
                document.querySelector("#password").focus();
            } else if (document.activeElement === document.querySelector("#password")) {
                login();
            }
        }
    }
</script>

<div class="login-form">
    <label>
        Логин:
        <input
            id="username"
            type="text"
            bind:value={username}
            placeholder="Введите логин"
            on:keydown={handleKeydown}
        />
    </label>
    <label>
        Пароль:
        <input
            id="password"
            type="password"
            bind:value={password}
            placeholder="Введите пароль"
            on:keydown={handleKeydown}
        />
    </label>
    <button on:click={login} class="login-button">Войти</button>
    {#if message}
        <p class="error-message">{message}</p>
    {/if}
</div>

<style>
    .login-form {
        display: flex;
        flex-direction: column;
        max-width: 400px;
        margin: 20px auto;
        padding: 20px;
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .login-form label {
        margin-bottom: 15px;
        font-size: 16px;
        color: #333;
    }

    .login-form input {
        width: 100%;
        padding: 10px;
        font-size: 14px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .login-form input:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    }

    .login-button {
        background-color: #007bff;
        color: white;
        padding: 10px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .login-button:hover {
        background-color: #0056b3;
    }

    .error-message {
        margin-top: 10px;
        color: red;
        font-size: 14px;
        text-align: center;
    }
</style>