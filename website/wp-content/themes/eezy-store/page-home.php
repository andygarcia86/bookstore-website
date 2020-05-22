<?php
get_header(); ?>

<div class="row">
	<div class="col-sm-12">
		<div id="primary" class="content-area">
			<main id="main" class="site-main" role="main">

				<h1>Books</h1>

				<div>
					<?php  
					$greetings = __('hello', 'my-text-domain');
					echo($greetings);

					?>
				</div>

			</main><!-- #main -->
		</div><!-- #primary -->
	</div>
	<!--col-md-8 col-xs-12 -->

	<?php
	get_footer();
