using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;
using Creo.ViewModels.MeetingAttendance;

namespace Creo.Controllers
{
	public class HomeController : Controller
	{
		public ActionResult Index( )
		{
			MeetingAttendanceList view = new MeetingAttendanceList( );


			return View( );
		}

		public ActionResult About( )
		{
			ViewBag.Message = "foobar.";

			return View( );
		}

		public ActionResult Contact( )
		{
			ViewBag.Message = "Your contact page.";

			return View( );
		}

		public ActionResult CouncillorsAttendance( )
		{
			return View( );
		}
	}
}