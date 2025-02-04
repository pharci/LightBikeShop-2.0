<script>
  import { Router } from 'svelte-routing';
  import Header from './components/Header.svelte';
  import Footer from './components/Footer.svelte';
  import MobileNav from './components/MobileNav.svelte';
  import { onMount } from "svelte";

  import { setUser, clearUser } from './stores/auth.js';

  async function checkAuth() {
    const res = await fetch("/api/me", {
      method: 'GET',
      credentials: 'same-origin',
    });

    if (res.ok) {
      const userData = await res.json();
      setUser(userData);
    } else {
      clearUser();
    }
  }

  onMount(() => {
    checkAuth();
  });
</script>

<Router>
  <Header/>
  <MobileNav />
  <Footer />
</Router>