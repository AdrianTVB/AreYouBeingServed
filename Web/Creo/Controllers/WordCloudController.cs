using Creo.ViewModels.Images;
using System.Collections.Generic;
using System.Web.Mvc;

namespace Creo.Controllers
{
	public class WordCloudController : Controller
	{

		private const int NapierCityCouncilId = 17;


		// GET: WordCloud
		[OutputCache( Duration = 86400, VaryByParam = "organisationid" )]
		public ActionResult Index( int organisationId )
		{
			List<WordCloudImage> images = new List<WordCloudImage>( );
			string path = "~/Images";
			if ( organisationId == NapierCityCouncilId )
			{
				ViewBag.Title = "Napier City Council";
				path += "/Napier";
				images.Add( new WordCloudImage( path + "/napier_" + 0 + ".png" ) );
			}
			else
			{
				ViewBag.Title = "Hastings District Council";
				path += "/Hastings";
				images.Add( new WordCloudImage( path + "/wordcloudHastings.png" ) );
			}

			return View( images );
		}
	}
}