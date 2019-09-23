using AutoMapper;
using Creo.ViewModels.Official;
using Domain.EntityFramework;

namespace Creo.Mappings
{
	public class OfficialProfile : Profile
	{
		public OfficialProfile( )
		{
			CreateMap<representative, OfficialListItem>( ); 
		}
	}
}