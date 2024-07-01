import { QueryConfig } from '../config';
import { Property } from '../property';
import { PropIndex } from '../propindex';
import { Wildcard } from '../wildcard';
import { Schema } from '../schema';
import { EncodingQueryBase } from '../query/encoding';
/**
 * Abstract interface for a constraint.
 */
export interface AbstractConstraint {
    name: string;
    description: string;
    properties: Property[];
    /**
     * Whether this constraint requires all specified properties types to be specific
     * in order to call satisfy function.
     */
    allowWildcardForProperties: boolean;
    /**
     * Whether this constraint is strict (not optional).
     */
    strict: boolean;
}
/**
 * Abstract model for a constraint.
 */
export declare class AbstractConstraintModel {
    protected constraint: AbstractConstraint;
    constructor(constraint: AbstractConstraint);
    name(): string;
    description(): string;
    properties(): Property[];
    strict(): boolean;
}
/**
 * Collection of constraints for a single encoding mapping.
 */
/** A method for satisfying whether the provided encoding query satisfy the constraint. */
export interface EncodingConstraintChecker<E extends EncodingQueryBase> {
    (encQ: E, schema: Schema, encWildcardIndex: PropIndex<Wildcard<any>>, opt: QueryConfig): boolean;
}
export declare class EncodingConstraintModel<E extends EncodingQueryBase> extends AbstractConstraintModel {
    constructor(constraint: EncodingConstraint<E>);
    hasAllRequiredPropertiesSpecific(encQ: E): boolean;
    satisfy(encQ: E, schema: Schema, encWildcardIndex: PropIndex<Wildcard<any>>, opt: QueryConfig): boolean;
}
/** Constraint for a single encoding mapping */
export interface EncodingConstraint<E extends EncodingQueryBase> extends AbstractConstraint {
    /** Method for checking if the encoding query satisfies this constraint. */
    satisfy: EncodingConstraintChecker<E>;
}
