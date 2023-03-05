import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
	'https://yqyheutdblzkrxymbhpw.supabase.co',
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlxeWhldXRkYmx6a3J4eW1iaHB3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY3NzM0ODE4NSwiZXhwIjoxOTkyOTI0MTg1fQ.tUvyX5eF_O6PskqI74IGPpZKoVwmM3_jR_7pr9CjqVg'
);
