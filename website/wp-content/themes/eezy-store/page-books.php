<?php
get_header(); ?>

<div class="row">
	<div class="col-sm-12">
		<div id="primary" class="content-area">
			<main id="main" class="site-main" role="main">

				<h1>Books</h1>

				<div>
					<?php $loop = new WP_Query(array('post_type' => 'book', 'posts_per_page' => 10)); ?>

					<?php while ($loop->have_posts()) : $loop->the_post(); ?>

						<div class="col-lg-3">
							<?php the_title('<h2 class="book-title"><a href="' . get_permalink() . '" title="' . the_title_attribute('echo=0') . '" rel="bookmark">', '</a></h2>'); ?>

							<div class="book-author-name">
								<?php
								/*
								$author_post_id = get_field("book_author");
								if ($author_post_id) {
									$author_name = get_the_title($author_post_id);
									echo $author_name;
								}
								*/
								?>
							</div>

							<div class="doc-profile">
								<?php the_post_thumbnail('thumbnail'); ?>
							</div>
						</div>

					<?php endwhile; ?>
				</div>

			</main><!-- #main -->
		</div><!-- #primary -->
	</div>
	<!--col-md-8 col-xs-12 -->

	<?php
	get_footer();
