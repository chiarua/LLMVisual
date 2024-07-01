import { PropIndex } from '../propindex';
import { ValueQuery } from '../query/encoding';
import { EncodingConstraintModel } from './base';
export declare const VALUE_CONSTRAINTS: EncodingConstraintModel<ValueQuery>[];
export declare const VALUE_CONSTRAINT_INDEX: {
    [name: string]: EncodingConstraintModel<ValueQuery>;
};
export declare const VALUE_CONSTRAINTS_BY_PROPERTY: PropIndex<EncodingConstraintModel<ValueQuery>[]>;
