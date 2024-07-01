import { QueryConfig } from '../config';
import { SpecQueryModel } from '../model';
import { Property } from '../property';
import { Schema } from '../schema';
import { Wildcard } from '../wildcard';
import { AbstractConstraint, AbstractConstraintModel } from './base';
export interface SpecConstraintChecker {
    (specM: SpecQueryModel, schema: Schema, opt: QueryConfig): boolean;
}
export declare class SpecConstraintModel extends AbstractConstraintModel {
    constructor(specConstraint: SpecConstraint);
    hasAllRequiredPropertiesSpecific(specM: SpecQueryModel): boolean;
    satisfy(specM: SpecQueryModel, schema: Schema, opt: QueryConfig): boolean;
}
export interface SpecConstraint extends AbstractConstraint {
    /** Method for checking if the spec query satisfies this constraint. */
    satisfy: SpecConstraintChecker;
}
export declare const SPEC_CONSTRAINTS: SpecConstraintModel[];
export declare const SPEC_CONSTRAINT_INDEX: {
    [name: string]: SpecConstraintModel;
};
/**
 * Check all encoding constraints for a particular property and index tuple
 */
export declare function checkSpec(prop: Property, wildcard: Wildcard<any>, specM: SpecQueryModel, schema: Schema, opt: QueryConfig): string;
