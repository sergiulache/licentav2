<script>
	import '../app.css';
	import NavbarFull from '../components/navbarFull.svelte';
</script>

<svelte:head>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');
		/* import Golos text font */
		@import url('https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700;800;900&display=swap');
	</style>
	<link
		href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.3/flowbite.min.css"
		rel="stylesheet"
	/>
</svelte:head>

<main>
	<NavbarFull />
	<slot />
</main>

<style>
	main {
		display: flexbox;
		height: 100%;
		width: 100%;
		place-items: center;
		align-items: center;
		/*background: linear-gradient(-135deg, #c850c0, #4158d0); */
	}

	/* set font family */
	* {
		font-family: 'Golos text', sans-serif;
	}
</style>
