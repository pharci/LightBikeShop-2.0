import { writable } from 'svelte/store';

export const user = writable(null);

export const setUser = (userData) => user.set(userData);
export const clearUser = () => user.set(null);