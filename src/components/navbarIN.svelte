<script>
	import NavbarAuctions from './navbarAuctions.svelte';
	import NavbarBrowse from './navbarBrowse.svelte';
	import NavbarCustomers from './navbarCustomers.svelte';
	import NavbarList from './navbarList.svelte';
	import NavbarNewAuctions from './navbarNewAuctions.svelte';
	import NavbarNotifications from './navbarNotifications.svelte';
	import NavbarProfile from './navbarProfile.svelte';
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
	<NavbarSignOut />
	<NavbarProfile />
</NavbarList>
