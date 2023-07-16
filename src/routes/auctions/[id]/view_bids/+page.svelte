<script>
	import { onMount } from 'svelte';
	import { supabase } from '$lib/supabaseClient';
	import { goto } from '$app/navigation';
	import { userSession } from '../../../../stores/userSession.js';
	import { browser } from '$app/environment';
	import { get } from 'svelte/store';
	import BidsTable from '../../../../components/bidsTable.svelte';

	export let data;
</script>

<BidsTable {data} />
