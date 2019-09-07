using Domain.EntityFramework;
using System;
using System.Linq;

namespace CoreEtl.Transform.ToDatabase
{
	public class ConverterHelper
	{
		public Organisation GetOrCreateOrganisation( creo_dbEntities dbContext, string orgName )
		{
			string orgNameRefined = orgName.ToLower( ).Trim( );
			Organisation org = dbContext.Organisations.FirstOrDefault( o => o.Name.ToLower( ) == orgNameRefined );
			if ( org == null )
			{
				dbContext.Organisations.Add( org = new Organisation( ) { Name = orgName } );
				dbContext.SaveChanges( );
			}
			return org;
		}

		public Meeting GetOrCreateMeeting( creo_dbEntities dbContext, string meetingName, DateTime date, Organisation organisation )
		{
			string meetingNameRefined = meetingName.ToLower( ).Trim( );
			Meeting org = dbContext.Meetings.FirstOrDefault( o => o.Name.ToLower( ) == meetingNameRefined && o.Date == date );
			if ( org == null )
			{
				org = new Meeting( ) { Name = meetingName, Date = date, Organisation = organisation };
				dbContext.Meetings.Add( org );
				dbContext.SaveChanges( );
			}
			return org;
		}

		public Official GetOrCreateOfficial( creo_dbEntities dbContext, string officialName, Organisation organisation )
		{
			string meetingNameRefined = officialName.ToLower( ).Trim( );
			Official org = dbContext.Officials.FirstOrDefault( o => o.Name.ToLower( ) == meetingNameRefined );
			if ( org == null )
			{
				org = new Official( ) { Name = officialName  };
				dbContext.Officials.Add( org );
				dbContext.SaveChanges( );
			}
			return org;
		}
	}
}
