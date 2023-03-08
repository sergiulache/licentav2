<script>
	import ItemBox from '../../components/itemBox.svelte';
	export let data;
</script>

<div class="p-4 sm:ml-64">
	<div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
		<ItemBox data={data.items} />
	</div>
</div>
