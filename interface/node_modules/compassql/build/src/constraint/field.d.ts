import { PropIndex } from '../propindex';
import { AutoCountQuery, FieldQuery } from '../query/encoding';
import { EncodingConstraintModel } from './base';
export declare const FIELD_CONSTRAINTS: EncodingConstraintModel<FieldQuery>[];
export declare const FIELD_CONSTRAINT_INDEX: {
    [name: string]: EncodingConstraintModel<FieldQuery | AutoCountQuery>;
};
export declare const FIELD_CONSTRAINTS_BY_PROPERTY: PropIndex<EncodingConstraintModel<FieldQuery>[]>;
