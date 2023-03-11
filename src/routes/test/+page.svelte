<script>
	import { userSession } from 'C:/Users/Sergiu/Documents/code/testing/fresh/licentav2/src/stores/userSession.js';

	let loggedIn = $userSession;
	console.log('------------');
	console.log(loggedIn);
</script>

<div>
	{#if loggedIn}
		<h1>Logged in</h1>
	{:else}
		<h1>Not logged in</h1>
	{/if}
</div>
