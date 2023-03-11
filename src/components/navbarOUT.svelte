<script>
	import NavbarBrowse from './navbarBrowse.svelte';
	import NavbarList from './navbarList.svelte';
	import NavbarLogIn from './navbarLogIn.svelte';
	import NavbarRegister from './navbarRegister.svelte';
	import NavbarToggleBtn from './navbarToggleBtn.svelte';
</script>

<NavbarToggleBtn />

<NavbarList>
	<NavbarBrowse />
	<NavbarLogIn />
	<NavbarRegister />
</NavbarList>
