using AutoMapper;
using Creo.ViewModels.MeetingAttendance;
using Domain.EntityFramework;

namespace Creo.Mappings
{
	public class MeetingProfile : Profile
	{
		public MeetingProfile( )
		{
			CreateMap<Meeting, MeetingAttendanceListItem>( )
				.ForMember( dest => dest.Organisation, opt => opt.MapFrom( s => s.Organisation.Name ) );
		}
	}
}