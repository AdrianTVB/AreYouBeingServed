//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace Domain.EntityFramework
{
    using System;
    using System.Collections.Generic;
    
    public partial class meetingType
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public meetingType()
        {
            this.meetingRepRelationships = new HashSet<meetingRepRelationship>();
            this.meetings = new HashSet<meeting>();
            this.meetingTypeScrapeHelpers = new HashSet<meetingTypeScrapeHelper>();
        }
    
        public int meetTypeID { get; set; }
        public string meetName { get; set; }
    
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<meetingRepRelationship> meetingRepRelationships { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<meeting> meetings { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<meetingTypeScrapeHelper> meetingTypeScrapeHelpers { get; set; }
    }
}