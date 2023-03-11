import { writable } from 'svelte/store';

export const userSession = writable(null);

// subscribe to changes in the `userSession` store

userSession.subscribe((value) => {
	console.log('userSession changed:', value);
});
