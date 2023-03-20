<script>
	export let data;
</script>

<div class="p-4 sm:ml-64">
	<div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
		<h1>Items:</h1>
		<ul>
			{#each data.items as item}
				<li>{item.title}: {item.description}</li>
			{/each}
		</ul>
	</div>
</div>
