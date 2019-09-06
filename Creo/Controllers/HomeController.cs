using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;
using CoreEtl.Models.FromScraper;

namespace Creo.Controllers
{
	public class HomeController : Controller
	{
		public ActionResult Index( )
		{
			using ( var reader = new StreamReader( @"C:\test.csv" ) )
			{
				List<MeetingAttendance> Organisation = new List<MeetingAttendance>( );
				List<MeetingAttendance> Date = new List<MeetingAttendance>( );
				List<MeetingAttendance> Meeting = new List<MeetingAttendance>( );
				while ( !reader.EndOfStream )
				{
					var line = reader.ReadLine( );
					var values = line.Split( ';' );

					Organisation.Add( values[ 0 ] );
					Date.Add( values[ 1 ] );
					Meeting.Add(values[2]);
				}
			}

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
	}
}