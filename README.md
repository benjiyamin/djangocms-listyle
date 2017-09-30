# Django CMS ListyleAdds a plugin to embed an ordered or unordered list to Django CMS. Children are automatically wrapped in `<li>` tags.The plugin extends the [Django CMS Style](https://github.com/divio/djangocms-style) plugin in order to make the same configurations available (index, classes, etc..)## UsageLet say you want to build a set of social buttons like in the following example, which requires rendering an unordered list of elements:![Social Buttons Example](./docs/img/social_buttons_example.png "Social Buttons Example")The HTML being for the button row being:	<ul class="list-inline intro-social-buttons">		<li>			<a href="#" class="btn btn-default btn-lg network-name" role="button">				<span class="icon fa fa-twitter" aria-hidden="true"></span>				twitter			</a>		</li>		<li>			<a href="#" class="btn btn-default btn-lg network-name" role="button">				<span class="icon fa fa-github" aria-hidden="true"></span>				GitHub			</a>		</li>		<li>			<a href="#" class="btn btn-default btn-lg network-name" role="button">				<span class="icon fa fa-linkedin" aria-hidden="true"></span>				linkedin			</a>		</li>		<li>			<a href="#" class="btn btn-default btn-lg network-name" role="button">				<span class="icon fa fa-envelope-o" aria-hidden="true"></span>				email			</a>		</li>	</ul>Using the Django CMS Listyle plugin, we can easily nest any listed objects.![Social Buttons Plugin Example](./docs/img/social_buttons_plugin_example.png "Social Buttons Plugin Example")What a time to be alive.## LicenseThis project is licensed under GPL 3.0 - see [LICENSE](LICENSE.md) for details.