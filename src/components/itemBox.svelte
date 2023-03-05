<script>
    export let data;
</script>

<div class="grid grid-cols-2 gap-4 mb-4">
    {#each data as item}
         <div class="flex items-center justify-center flex-col  bg-gray-50 h-28 dark:bg-gray-800 rounded-2xl border-2 border-gray-400 border-dotted">
            <p class="text-2xl text-black dark:text-gray-500">{item.name}</p>
            <p class="overflow text-xl text-gray-400 dark:text-gray-500 p-3">{item.description}</p>
         </div>
    {/each}
</div>

<style>
    .overflow {
	display: -webkit-box;
    max-width: 780px;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
	
    
</style>