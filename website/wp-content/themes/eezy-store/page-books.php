<?php
get_header(); ?>

<div class="row">
	<div class="col-sm-12">
		<div id="primary" class="content-area">
			<main id="main" class="site-main" role="main">

				<h1>Books</h1>

				<a href="<?php echo(get_site_url()); ?>/change-lang?lang=es_ES">Español</a>
				<br/><br/>
				<a href="<?php echo(get_site_url()); ?>/change-lang?lang=en_US">English</a>
				<br/><br/>

				<?php 
				$var1 = get_locale();
				echo $var1;
				echo "<br/>";

				?>

				<?php
				_e('hello_world', 'eezy-store');

				$domain = 'eezy-store';

				// $greetings = __('hello', $domain);
				// echo ($greetings);

				/* Get the translation and echo */
				// _e('hello', $domain);

				// $html = esc_html__("<a href='www.google.com'>A link</a>")
				// echo ($html);

				// esc_html_e("<a href='www.google.com'>A link</a>")

				// $user = "Carol";
				// $employee_number = 99;
				// $greetings = sprintf(__('hello %s you are employee number %d.', $domain), $user, $employee_number);
				// echo $greetings;

				// $arg1 = 'this';
				// $arg2 = 'that';
				// $format = 'I present you %2$s and %1$s';
				// $result = sprintf(__($format, $domain), $arg1, $arg2);
				// echo($result);

				// $number_of_comments = 2;
				// $text = _n('There is a %d comment', 'There are %d comments', $number_of_comments, $domain);
				// $result = sprintf($text, $number_of_comments);
				// echo($result);

				?>

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
