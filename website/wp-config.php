<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'bookstore_website' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', '' );

/** MySQL hostname */
//define( 'DB_HOST', 'localhost:3309' );  // Laptop conx
define( 'DB_HOST', 'localhost' ); // Desctop conx

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'fdI6v7;qSuNfQPM+(9-ioOA7& z{#}c]0F&3]3{}u3Tn*Zz^#c8 Y+ybDXeFzNAT' );
define( 'SECURE_AUTH_KEY',  'ei3Ge0o;2}B8VfAquF}Ju%$= %#w_|>QId:KGNklAE.*v;H>&yIK^or9?YS9Z_qa' );
define( 'LOGGED_IN_KEY',    'K`q/Pr={9iIBo5X^2X/<cw;nN?Yn@++Ar~wF^b,g@9WeD5jz7xs4i5%;ecx4sXrv' );
define( 'NONCE_KEY',        'epoUxrmBFLwh6G;^%&E4bLFM`>eJQT+ZLx<D_}5IHe+s^{C1l&x#NF.|-g|?NV4?' );
define( 'AUTH_SALT',        '2lst8f*@[Zr1*kG,Fi={oan&[SV<gq*~_31<tb ,aWvzeiE6kTOp8{}}c+spaUZ0' );
define( 'SECURE_AUTH_SALT', '^!(R6X>Yokx^49~u^!-3J%tFnjtX3aKU?-c5R3x6RDJ{|,;DB9Ej>l#S/~V%nX}m' );
define( 'LOGGED_IN_SALT',   'IKT`f{y/b`g&5=ShDqU;^4|m:;5b.R&o2?>)zXBId%n@E4;DwL[7_i2^46;A|$:i' );
define( 'NONCE_SALT',       '@7ae8Css4,xrm35LlRXrPzB!9$Zw8JJ#pxaddTqIp%5cNH$kNYkq7Ev-p,=_ $./' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'bs_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
