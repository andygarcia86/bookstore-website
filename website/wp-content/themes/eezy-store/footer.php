<?php
/**
 * The template for displaying the footer.
 *
 * Contains the closing of the #content div and all content after.
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package eezy-store
 */

?>
		</div><!-- #content -->
	</div><!-- #page -->
</div><!-- .container -->

<div class="container-fluid eezy-ftr-clr">
	
	<div class="container">

		<footer id="colophon" class="site-footer" role="contentinfo">
		
			<div id="inner-footer" class="clearfix">
				<div class="row">				
						
				</div> 
			</div>
		
			<div class="site-info">
				<div class="footer-menu">
					<?php wp_nav_menu( array( 'menu_id' => 'footer' , 'container_class'=> 'eezy-store-nav') ); ?>
				</div>

				<ul class="social-menu">
					<li>
						<a href="https://www.facebook.com/" target="_blank"><i class="fa fa-facebook"></i></a>
						<a href="https://www.youtube.com/" target="_blank"><i class="fa fa-youtube"></i></a>
						<a href="https://github.com/" target="_blank"><i class="fa fa-github"></i></a>
					</li>
				</ul>

				<div class="clearfix">
				</div>

			</div><!-- .site-info -->
			
		</footer><!-- #colophon -->
	</div><!-- #container -->
</div>

<?php wp_footer(); ?>

</body>
</html>