using System.Collections.Generic;
using System.Web.Mvc;
using Creo.ViewModels.MeetingAttendance;
using Creo.ViewModels.Official;

namespace Creo.Controllers
{
	public class HomeController : Controller
	{
		public ActionResult Index( )
		{
			MeetingAttendanceList vm = new MeetingAttendanceList( );
			vm.Attendees = new List<OfficialListItem>( );

			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Boag", Attendances = 4, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Councillor-Maxine-Boag-Oct-2016-5.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 2, Name = "Brosnan", Attendances = 4, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Councillor-Annette-Brosnan-Oct-2016-7.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 2, Name = "Dallimore", Attendances = 4 } );
			vm.Attendees.Add( new OfficialListItem { Id = 2, Name = "Dalton", Attendances = 1, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Mayor-Bill-Dalton-Oct-2016-3.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Hague", Attendances = 4 } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Jeffrey", Attendances = 4, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Councillor-Tony-Jefferies-Mar-2017-2.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "McGrath", Attendances = 4, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Councillor-Richard-McGrath-Oct-2016-2.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Price", Attendances = 4, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Councillor-Keith-Price-Oct-2016-2.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Tapine", Attendances = 4 } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Taylor", Attendances = 4 } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "White", Attendances = 4, ProfileImageUrl = "https://napier.govt.nz/assets/Contacts/Councillor-Faye-White-Oct-2016.jpg" } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Wise", Attendances = 4 } );
			vm.Attendees.Add( new OfficialListItem { Id = 1, Name = "Wright", Attendances = 1 } );

			return View( vm );
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