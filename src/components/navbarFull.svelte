<script>
	import NavbarAuctions from './navbarAuctions.svelte';
	import NavbarBrowse from './navbarBrowse.svelte';
	import NavbarCustomers from './navbarCustomers.svelte';
	import NavbarList from './navbarList.svelte';
	import NavbarLogIn from './navbarLogIn.svelte';
	import NavbarNewAuctions from './navbarNewAuctions.svelte';
	import NavbarNotifications from './navbarNotifications.svelte';
	import NavbarRegister from './navbarRegister.svelte';
	import NavbarSignOut from './navbarSignOut.svelte';
	import NavbarToggleBtn from './navbarToggleBtn.svelte';
</script>

<NavbarToggleBtn />

<NavbarList>
	<NavbarBrowse />
	<NavbarAuctions />
	<NavbarNewAuctions />
	<NavbarNotifications />
	<NavbarCustomers />
	<NavbarLogIn />
	<NavbarRegister />
	<NavbarSignOut />
</NavbarList>
